import openreview

# API V2
client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username="jw2yang@gatech.edu",
    password="yjw1002070119"
)

venue_id = "thecvf.com/CVPR/2025/Workshop/CVinW"

profile_ids = [
    '~Jianwei_Yang1',
    '~Chunyuan_Li1',
    '~Jiasen_Lu2',
    '~Reuben_Tan1',
    '~Mu_Cai1',
    '~Xuehai_He1',
    '~Hao_Zhang39',
    '~Tianhe_Ren1',
    '~Feng_Li9',
    '~Shilong_Liu1',
    '~Xueyan_Zou1',
    '~Zhengyuan_Yang1',
    '~Xin_Eric_Wang2',
    '~Yong_Jae_Lee2',
    '~Lei_Zhang23',
    '~Jianfeng_Gao1',
]

client.impersonate(venue_id)

for profile_id in profile_ids:
    profiles = openreview.tools.get_profiles(client, [profile_id]) # you can also pass a list containing multiple profile ids or email addresses
    user_email = profiles[0].get_preferred_email()
    print(user_email)