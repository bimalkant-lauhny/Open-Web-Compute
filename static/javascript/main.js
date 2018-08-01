$(document).ready(function(){
	$(".form-select").on('change', function() {
		if (this.value == "filterby") {
			console.log(this.value)
			let label = $("<label>Enter the filter condition:</label>");
			$(".select-form").append(label);
			let criteria = $('<input id="filterinput" type="text" name="criteria" placeholder="Enter Condition">');
			$(".select-form").append(criteria);	
		} else {
			console.log(this.value);
			$("#filterinput").remove();	
		}
	});
}); 