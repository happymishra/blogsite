$.ajax({
    url:"/blog/api/bloglist/",
    success: function(result){
        console.log(result);
        createBlogStructure(result);

    },
    error: function(xhr, status, error){
        console.log(status);
        console.log(error);
    }
})

//This function displays the list of blog and its creates the blog divs dynamically
function createBlogStructure(response){
    var parentId = $('#listBlog');
	$.each(response, function(key, value){
	    var div = $('<div>', {
	        id: value['pk']
        });
	    parentId.append(div);

	    var blog_text = value.fields.text
        var blog_title = value.fields.title

		var titleDiv = $('<div>', {
		    text: blog_title,
            class:'blog-title'
        })

        div.append(titleDiv);

		var divBlogContent = $('<div>', {
			text: blog_text,
            class:"blog-text"
		})
        div.append(divBlogContent);

		//Edit button
		var editButton = $('<button/>', {
		    text: "Edit",
            click: editBlog
        })
        div.append(editButton)

        //Delete button
        var deleteButton = $('<button/>', {
		    text: "Delete",
            click: deleteBlog
        })
        div.append(deleteButton)
	});

    //Create button
    var createButton = $('<button/>', {
        text: "Create",
        click: createBlog
    })
    parentId.append(createButton)
}

//Edit blog function
function editBlog(){
    var pId = $(this).parent().attr('id');
    //Populate the form with the exiting blog data
    document.getElementById('edit-blog-text').innerHTML = $('#'+pId).find(".blog-text").text();
    document.getElementById('blog-id').value = pId

    //Code to display the edit form pop up
    var modal = document.getElementById('myModal');
    modal.style.display = "block";
    //When the user clicks on the close button
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
        modal.style.display = "none";
    }
    // When the use clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}


//Delete blog
function deleteBlog(){
    var pId = $(this).parent().attr('id');
    $.ajax({
        url:'/blog/api/delete/' + pId + '/',
        success: function(){
            //Reload the page to get the refreshed data
            window.location.reload();
            console.log("Deletion successful");
        },
        error:function(status){
            console.log("Deletion failed"+ status);
        }
    })
}

//Create blog
function createBlog(){
    window.location = "/blog/create/";
}
