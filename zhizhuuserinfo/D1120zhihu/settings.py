# -*- coding: utf-8 -*-

# Scrapy settings for D1120zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'D1120zhihu'

SPIDER_MODULES = ['D1120zhihu.spiders']
NEWSPIDER_MODULE = 'D1120zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   #'Accept-Language': 'en',
   #浏览网页中获取头文件
    ':authority': 'www.zhihu.com',
    ':method': 'GET',
    #':path': '/api/v4/members/chen-jun-15-6/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20',
    ':scheme': 'https',
    'accept': '*/*',
    #'accept-encoding': 'gzip, deflate, br', #会导致无法对respnose.body解码
    'accept-language': 'zh,zh-CN;q=0.9',
    'cookie': '_zap=8196a72e-7a16-4787-a0dd-1fd72b0bdec2; _xsrf=9jMOWTZIp8fSYVhrkuMCaSkB9njNpaIQ; d_c0="AHAmnns4Ug6PTjLdTQ8UEYRfnZ6P7Rr82qw=|1538815902"; q_c1=694d278bb9f24f058017eb6efedab7c0|1538815932000|1538815932000; __utma=51854390.2004417295.1539450390.1539450390.1539450390.1; __utmc=51854390; __utmz=51854390.1539450390.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20160821=1^3=entry_date=20160821=1; tst=r; capsion_ticket="2|1:0|10:1541417450|14:capsion_ticket|44:NTRiNThkN2JlN2RiNDk4YTgwYzBiYWU2ZmZmOTc2MGY=|c2b626aaebdd2a23587503c752ab42cd8943096955f0ef421664d32679e02977"; z_c0="2|1:0|10:1541417489|4:z_c0|92:Mi4xN2dkZ0F3QUFBQUFBY0NhZWV6aFNEaWNBQUFDRUFsVk5FYmNIWEFDa2NuenBvRDhyM1dOOG01SWhnamM3TUhvQTl3|ca1c34ca086354c2edcb9011ad93fc6e215d18c46187fcaec54aabac6a710215"; tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c',
    'referer': 'https://www.zhihu.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'x-ab-param': 'top_hweb=0;top_recommend_topic_card=0;se_dt=1;top_nmt=0;top_quality=0;top_nid=0;se_consulting_price=n;top_bill=0;top_followtop=1;top_nszt=0;top_tffrt=0;top_sjre=0;tp_discussion_feed_type_android=0;se_new_market_search=off;se_relevant_query=new;se_tf=1;top_ac_merge=0;top_root_ac=1;top_billboard_count=1;top_spec_promo=1;zr_ans_rec=gbrank;se_cq=1;se_majorob_style=0;se_major_onebox=major;se_gi=0;ls_new_video=1;se_filter=0;top_nucc=3;top_universalebook=1;top_video_score=1;se_rescore=1;se_entity=on;top_new_feed=1;se_correct_ab=1;se_gemini_service=content;top_billupdate1=3;top_recall_tb_long=51;top_videos_priority=-1;se_ad_index=9;top_root=1;top_slot_ad_pos=1;top_tuner_refactor=-1;top_sj=2;se_engine=0;top_pfq=5;top_login_card=1;top_video_rew=0;top_recall_tb_short=61;top_vd_rt_int=0;se_billboard=0;top_tr=2;tp_sft=a;se_wiki_box=1;top_alt=0;top_mlt_model=0;top_newfollowans=0;se_billboardsearch=0;top_recall_tb_follow=71;top_root_mg=1;se_refactored_search_index=0;se_websearch=0;top_free_content=-1;top_promo=1;top_deep_promo=0;top_feedre_itemcf=31;top_gif=0;se_backsearch=0;se_minor_onebox=d;top_lowup=1;top_memberfree=1;top_mt=0;top_vds_alb_pos=0;top_fqai=2;top_gr_topic_reweight=0;top_recall_deep_user=1;top_roundtable=1;se_dl=1;top_follow_reason=0;tp_ios_topic_write_pin_guide=1;top_hqt=9;top_rerank_repos=-1;se_merger=1;se_daxuechuisou=new;top_rerank_isolation=-1;top_f_r_nb=1;top_recall_core_interest=81;top_ad_slot=1;top_ebook=0;pin_efs=orig;top_feedtopiccard=0;tp_write_pin_guide=3;ls_is_use_zrec=0;top_billpic=0;top_no_weighing=1;se_product_rank_list=0;top_feedre_cpt=101;top_manual_tag=1;top_vd_gender=0;top_dtmt=2;top_tag_isolation=0;top_ab_validate=2;top_wonderful=1;top_test_4_liguangyi=1;top_billab=1;top_yhgc=0;top_root_web=0;top_tagore=1;top_retag=0;top_v_album=1;top_user_gift=0;tp_discussion_feed_card_type=0;se_consulting_switch=off;top_gr_model=0;top_ntr=1;top_recall=1;top_recall_tb=3;top_nad=1;top_rerank_breakin=-1;top_tmt=0;top_topic_feedre=21;top_cc_at=1;tp_favsku=a;top_raf=n;top_root_few_topic=0;top_hca=0;top_local=1;top_nuc=0;ls_new_score=0;top_30=0;top_adpar=0;top_is_gr=0;se_ltr=1;top_fqa=0;top_gr_auto_model=0;top_multi_model=0;top_rank=1;top_yc=0;top_billread=1;top_feedre_rtt=41;top_newfollow=0;pin_ef=orig;top_new_user_gift=0;top_uit=0;top_vdio_rew=0;se_cm=1;top_retagg=0;top_vd_op=0;se_ingress=on;top_rerank_reweight=-1;top_distinction=4;top_video_fix_position=0;top_feedre=1;top_tagore_topic=0;se_auto_syn=0;top_billvideo=0;top_an=0;top_card=-1;top_recall_follow_user=91',
    'x-requested-with': 'fetch',
    'x-udid': 'AHAmnns4Ug6PTjLdTQ8UEYRfnZ6P7Rr82qw=',
    'x-zse-83': '3_1.1',
    'x-zse-84': 'g_NkP_KkR58bMorlgg9k0Ctl8trv62rmkobmTOow8tb_Oorwn58kR__lSoeuPoel',
    
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'D1120zhihu.middlewares.D1120ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'D1120zhihu.middlewares.D1120ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'D1120zhihu.pipelines.D1120ZhihuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
