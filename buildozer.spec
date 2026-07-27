[app]
title = Jarvix AI
package.name = jarvixai
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,speechrecognition,requests,urllib3,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, RECORD_AUDIO

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
