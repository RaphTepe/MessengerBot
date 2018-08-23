def image_grade1(fbid):
	
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
			        "template_type":"generic",
			        "elements":[
			           {
			            "title":"Welcome!",
			            "image_url":"https://petersfancybrownhats.com/company_image.png",
			            "subtitle":"We have the right hat for everyone.",
			            "default_action": {
			              "type": "web_url",
			              "url": "www.justdoeat.fr",
			              "webview_height_ratio": "tall",
			            },
			             
			          }
			        ]
			      }
			    }
			  }
			  })

	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	status = requests.post(post_message_url,  params=params, headers=headers, data=data)
	pprint(status.json())
