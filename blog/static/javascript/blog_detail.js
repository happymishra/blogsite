$.ajax({
    url:"/blog/api/bloglist/",
    success: function(result){
        createBlogStructure(result);

    },
    error: function(xhr, status, error){
        console.log(status);
    }
})
