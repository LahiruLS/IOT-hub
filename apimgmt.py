import networkdiscover
##################################################################################################
											#API Mangement#
##################################################################################################

def hande_GET_msg(msg):
	parameters = msg.split('&')
	catagory   = parameters[0].split('=')[1]
	option     = parameters[1].split('=')[1]
	device	   = parameters[2].split('=')[1]

	if(len(parameters)==4):
		if(parameters[3].split('=')[0]=='stat'):
			mode='stat'
			if(parameters[3].split('=')[1]=='0'):
				value=0
			else if(parameters[3].split('=')[1]=='1')
				value=1


		else if(parameters[3].split('=')[0]=='level'):
				mode='level'
				level = parameters[3].split('=')[1]



	if(catagory == 'led'):
		if(option=='blink'):
			#selecet device
			#send data
			#receive data

		else if(option=='switch'):
			##selecet device
			#send data
			#receive data

		else if(option=='dim'):
			#selecet device
			#send data
			#receive data