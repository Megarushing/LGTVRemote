# LG TV Remote for 2011 TVs

LG TV Remote is an iOS App capable of remotely controlling old LG Smart TVs via network connection.

It is compatible with models LV550x,LW550x,LW570x,LW650x,LV37xx

This app was built in Python with [Pythonista for iOS](http://omz-software.com/pythonista) based on [LGCommander](https://github.com/ubaransel/lgcommander) project by ubaransel

## List of Useful Control Codes

### Menus
	status_bar = 35
	quick_menu = 69
	home_menu = 67
	premium_menu = 89
	installation_menu = 207
	factory_advanced_menu1 = 251
	factory_advanced_menu2 = 255

### Power Control
	power_off = 8
	sleep_timer = 14

### Navigation
	left = 7
	right = 6
	up = 64
	down = 65
	select = 68
	back = 40
	exit = 91
	red = 114
	green = 113
	yellow = 99
	blue = 97

### Keypad
	"0" = 16
	"1" = 17
	"2" = 18
	"3" = 19
	"4" = 20
	"5" = 21
	"6" = 22
	"7" = 23
	"8" = 24
	"9" = 25
	underscore = 76

### Playback Controls
	play = 176
	pause = 186
	fast_forward = 142
	rewind = 143
	stop = 177
	record = 189

### Input Controls
	tv_radio = 15
	simplink = 126
	input = 11
	component_rgb_hdmi = 152
	component = 191
	rgb = 213
	hdmi = 198
	hdmi1 = 206
	hdmi2 = 204
	hdmi3 = 233
	hdmi4 = 218
	av1 = 90
	av2 = 208
	av3 = 209
	usb = 124
	slideshow_usb1 = 238
	slideshow_usb2 = 168

### TV Controls
	channel_up = 0
	channel_down = 1
	channel_back = 26
	favorites = 30
	teletext = 32
	t_opt = 33
	channel_list = 83
	greyed_out_add_button? = 85
	guide = 169
	info = 170
	live_tv = 158

### Picture Controls
	av_mode = 48
	picture_mode = 77
	ratio = 121
	ratio_4_3 = 118
	ratio_16_9 = 119
	energy_saving = 149
	cinema_zoom = 175
	"3d" = 220
	factory_picture_check = 252

### Audio Controls
	volume_up = 2
	volume_down = 3
	mute = 9
	audio_language = 10
	sound_mode = 82
	factory_sound_check = 253
	subtitle_language = 57
	audio_description = 145

## Pythonista Template

This code contains a (very) stripped down version of Pythonista App Template, with only the essential to run it with requests lib, this may be useful for learning what is really necessary to keep into the framework when releasing an App.


