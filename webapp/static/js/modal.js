$(document).ready(function(){
    $("#floatingSelectGrid").on("change", function () {        
        $modal = $('#exampleModal');
        if($(this).val() == 'add'){
            $modal.modal('show');
            $.ajax({
                type: 'GET',
                url: '/category/create',
                })
        }
    });
});