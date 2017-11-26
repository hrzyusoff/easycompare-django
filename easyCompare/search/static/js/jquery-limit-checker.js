var limit = 3;
$('input.checkbox-compare').change(function() {
       if($(this).is(":checked")).length >= limit {
          alert($(this).val())
          return;
       } 
}); 