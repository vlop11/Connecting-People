var limit = 3;

// $                 it's creating a access point
// .interest_form    selecting for class .interest_form
// ":checkbox"       this is selecting either type=checkbox or <checkbox> (which doesn't exist btw) in the html
// change()         if there's a change in the selected elements, run the function inside
// $this             applies to whatever html element was selected... in this case, what was clicked!
// closest("k")    finds the closest ancestor of 'this' which is a "k"
// find()          returns all __what's in the ()__ elements inside of the __what it was called on__
// ":checkbox:checked"  all elements that are checked check-boxes

$(".interest_form :checkbox").change(function(){
  // the next line returns a list of checked boxes
  clicked_checkboxes = $(this).closest(".interest_form").find(":checkbox:checked");
  // if the list has >3 checked boxes...
  if(clicked_checkboxes.length > limit) {
    // set this current button to false - it's not checked anymore!
    this.checked = false;
  }
});
