import json
from time import time, mktime
from datetime import datetime, timedelta
from collections import Counter
from foursquare.models import User, Venue, Zone, Checkin


# Function which returns today's date.
def get_datetime():
    return datetime.now().strftime("%Y%m%d")


# Function which returns the current timestamp.
def get_timestamp():
    return int(time())


# Function which returns the timestamp of a month ago.
def get_timestamp_month_ago():
    today = datetime.today()
    month_ago = today - timedelta(days=30)
    timestamp = mktime(month_ago.timetuple())

    return int(timestamp)


# Function which processes the information from the user and store it in the database.
def process_user(user):

    # Create a new user with the required information.
    new_user = User(id=user['id'],
                    first_name=user['firstName'],
                    last_name=user['lastName'],
                    gender=user['gender'],
                    photo=user['photo']['suffix'])

    # If the optional information has changed, it is updated.
    if 'homeCity' in user:
        new_user.city = user['homeCity']
    if 'bio' in user:
        new_user.bio = user['bio']
    if 'email' in user['contact']:
        new_user.email = user['contact']['email']
    if 'facebook' in user['contact']:
        new_user.facebook = user['contact']['facebook']
    if 'twitter' in user['contact']:
        new_user.twitter = user['contact']['twitter']

    # If the user exists, update his information.
    if User.objects.filter(id=user['id']):
        old_user = User.objects.get(id=user['id'])
        new_user.points = old_user.points
        new_user.num_zones = old_user.num_zones
        new_user.num_friends = old_user.num_friends

    # Finally, save the changes.
    new_user.save()

    return new_user


# Function which processes the information from the checkins and stored it in the database.
def process_checkins(user, checkins):
    # Create auxiliary variables.
    venues = []
    # For each instance create a Venue.
    for venue in checkins:
        # If the Venue exists in database, store it.
        if Venue.objects.filter(id=venue['venue']['id']):
            venues.append(Venue.objects.get(id=venue['venue']['id']))

    # Count the repetitions.
    count_checkins = Counter(venues)

    # For each id, store the checkins's number.
    for venue in list(count_checkins):
        # If the checkin exists, update the number.
        if Checkin.objects.filter(user=user, venue=venue):
            exist = Checkin.objects.get(user=user, venue=venue)
            exist.num_checkins = count_checkins[venue]
            exist.process = True
            exist.save()
        # Else, create it.
        else:
            Checkin(user=user,
                    venue=venue,
                    num_checkins=count_checkins[venue]).save()

    # For each checkin of the user.
    all_checkins = Checkin.objects.filter(user=user)
    for item in all_checkins:
        # If process is True.
        if item.process == True:
            # Change it to False.
            item.process = False
            item.save()
        #If process is False.
        else:
            # Delete the checkin.
            item.delete()


# Function which get and process the user's checkins from the database.
def get_data_database(user):
    checkins = Checkin.objects.filter(user=user)
    checkins_process = []

    for item in checkins:
        checkins_process.append(
           {'user': item.user.first_name + ' ' + item.user.last_name,
            'venue': {'name': item.venue.name,
                      'lat': item.venue.lat,
                      'lon': item.venue.lon},
            'num_checkins': item.num_checkins},)

    return {'checkins': checkins_process}
