def message_commande1(fbid):
	params = {
		'access_token':PAGE_ACCESS_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}
	data = json.dumps({
		"recipient": {
			"id": fbid
		},

		"message":{
			"attachment":{
			  "type":"template",
			  "payload":{
				"template_type":"button",
				"text":"Il ne te reste plus qu'à lier ton compte JustDoEat pour que tu puisses profiter de mes services. ",
				"buttons":[
				  {
					"type":"we_url",
					"url":"https://google.fr",
					"title": "Lier mon compte"
				  }
 
				]
			  }
			}
		  }
			})


	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	status = requests.post(post_message_url,  params=params, headers=headers, data=data)
	pprint(status.json())
