var updateBtns = document.getElementsByClassName('update-basket')

for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var clothesId = this.dataset.clothes
        var clubsId = this.dataset.clubs
        var accessoriesId = this.dataset.accessories
		var action = this.dataset.action
        console.log('clothesId:', clothesId, 'action:', action) 
        console.log('clubsId:', clubsId, 'action:', action)
        console.log('accessoriesId:', accessoriesId, 'action:', action)
        console.log("USER:", user)
        if(user == 'AnonymousUser'){
            console.log('Not Logged In')
        }else{
            console.log('User is logged in, sending data..')
        }
    })
}