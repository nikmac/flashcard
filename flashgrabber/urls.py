from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^$', 'flash_card.views.home', name='home'),
    url(r'^make_card/', 'flash_card.views.make_card', name='make_card'),
	url(r'^createCard/', 'flash_card.views.createCard', name='createCard'),
	url(r'^ocr/', 'flash_card.views.ocr', name='ocr'),
	url(r'^cardBox/', 'flash_card.views.viewCardList', name='cardBox'),
    url(r'^quiz/', 'flash_card.views.quiz', name='quiz'),
    url(r'^quiz_menu/', 'flash_card.views.quiz_menu', name='quiz-menu'),
    url(r'^quiz_score/', 'flash_card.views.quiz_score', name='quiz_score'),
    url(r'^card_score/', 'flash_card.views.card_score', name='card_score'),
    url(r'^maker_revamp/', 'flash_card.views.maker_revamp', name='maker_revamp'),
    url(r'^admin/', include(admin.site.urls)),
)
