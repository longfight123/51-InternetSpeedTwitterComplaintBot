"""Internet Speed Twitter Complaint Bot

This script automatically tweets a complaint about
the user's internet speed if it is below what was promised
by their service provider. This script requires the user have
a twitter account.

This script requires that 'selenium' and 'python_dotenv' be installed within the Python
environment you are running this script in.

"""

from InternetSpeedTwitterBot import InternetSpeedTwitterBot

internetspeedtwitterbot = InternetSpeedTwitterBot()
internetspeedtwitterbot.get_internet_speed()
internetspeedtwitterbot.tweet_at_provider()