  
$(document).ready(function(){
    console.log('hello world')
    $('#modal-btn').click(function(){
        console.log('working')
        $('.ui.modal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
})


$(function() {
  $("#places").autocomplete({
    source: "/api/get_places/",
    select: function (event, ui) { //item selected
      AutoCompleteSelectHandler(event, ui)
    },
    minLength: 2,
  });
});

function AutoCompleteSelectHandler(event, ui)
{
  var selectedObj = ui.item;
}

