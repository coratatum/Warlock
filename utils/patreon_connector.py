# Campaign ID can be fetched trough the API (List all Campaigns: GET https://www.patreon.com/api/oauth2/v2/campaigns)
# access_token can be created on https://www.patreon.com/portal/registration/register-clients

import patreon

def get_stuff():
    access_token = None # replace with access token -> get from gcp secrets

    api_client = patreon.API(access_token)
    # Get the campaign ID
    campaign_response = api_client.fetch_campaign()
    campaign_id = campaign_response.data()[0].id()

    # Fetch all pledges
    # OR alternatively call the endpoint directly? might be better approach to easily see the fields
    all_pledges = []
    cursor = None
    while True:
        pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)
        all_pledges += pledges_response.data()
        cursor = api_client.extract_cursor(pledges_response)
        if not cursor:
            break
    
    # discord_data = patreon_user['attributes']['social_connections']['discord']
    # https://www.patreon.com/api/oauth2/v2/campaigns/{campaign_id}/members?include=currently_entitled_tiers,address&fields[member]=full_name,patron_status