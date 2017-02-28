SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '86hxynarcwuu84'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'UnWH1SYDncmFhGs4'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['picture-url', 'email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'li_id'),
                               ('firstName', 'first_name'),
                               ('lastName', 'last_name'),
                               ('emailAddress', 'email_address'),
                               ('headline', 'headline'),
                               ('picture-url', 'picture_url')]

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.user.get_username',
#     'social.pipeline.user.create_user',
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'social.pipeline.user.user_details'
# )
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard'
SOCIAL_AUTH_LOGIN_URL = '/'
#SOCIAL_AUTH_URL_NAMESPACE = 'dashboard'

SOCIAL_AUTH_FACEBOOK_KEY = '172937386541784'
SOCIAL_AUTH_FACEBOOK_SECRET = '2210e06173b9f48c73091c5aa05dbe10'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#   'locale': 'ru_RU',
#   'fields': 'id, name, email, age_range'
# }