var updateBtns = document.getElementsByClassName('update-basket')

for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var golfgearId = this.dataset.golfgear
		var action = this.dataset.action
        console.log('golfgearId:', golfgearId, 'action:', action) 
        console.log("USER:", user)
        if(user == 'AnonymousUser'){
            updateGuestOrder(golfgearId, action)
        }else{
            updateUserOrder(golfgearId, action)
        }
    })
}

function updateGuestOrder(golfgearId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (basket[golfgearId] == undefined){
		basket[golfgearId] = {'quantity':1}

		}else{
			basket[golfgearId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		basket[golfgearId]['quantity'] -= 1

		if (basket[golfgearId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete basket[golfgearId];
		}
	}
    console.log('Basket:', basket)
}

function updateUserOrder(golfgearId, action){
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'golfgearId': golfgearId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}