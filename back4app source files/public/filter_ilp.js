// Get unique values for the desired columns

// {3 : ["ITS", "ALP"], 4 : [*Many], 5 : [*Many]}

function getUniqueValuesFromColumn() {

    var unique_col_values_dict = {}

    allFilters = document.querySelectorAll(".table_search-filter");
    table = document.querySelectorAll("#ilptable")[0];	
 let filterColumns = [];
 allFilters.forEach((ele) => { filterColumns.push(ele.getAttribute('col-index'))});

	const rows = document.querySelectorAll("#ilptable > tbody > tr")

	rows.forEach((row) => {
		filterColumns.forEach( (col_index) => { 
		cell_value = row.querySelector("td:nth-child("+col_index+")").innerHTML;
		
		// if the col index is already present in the dict
		if (col_index in unique_col_values_dict) {

			// if the cell value is already present in the array
			if (unique_col_values_dict[col_index].includes(cell_value)) {
				// alert(cell_value + " is already present in the array : " + unique_col_values_dict[col_index])

			} else {
				unique_col_values_dict[col_index].push(cell_value)
				// alert("Array after adding the cell value : " + unique_col_values_dict[col_index])
			}
		} else {
			unique_col_values_dict[col_index] = new Array(cell_value)
		}
		});		
	});  ;

    // for(i in unique_col_values_dict) {
        // alert("Column index : " + i + " has Unique values : \n" + unique_col_values_dict[i]);
    // }
    updateSelectOptions(unique_col_values_dict)
};

// Add <option> tags to the desired columns based on the unique values

function updateSelectOptions(unique_col_values_dict) {
    allFilters = document.querySelectorAll(".table_search-filter");
    table = document.querySelectorAll("#ilptable")[0];	
 let filterColumns = [];

    allFilters.forEach((filter_i) => {
        col_index = parseInt(filter_i.getAttribute('col-index'));

        unique_col_values_dict[col_index].forEach((i) => {
            filter_i.innerHTML = filter_i.innerHTML + `\n<option value="${i}">${i}</option>`
        });

    });
};


// Create filter_rows() function

// filter_value_dict {2 : Value selected, 4:value, 5: value}

function filter_rows() {
    allFilters = document.querySelectorAll(".table_search-filter");
    table = document.querySelectorAll("#ilptable")[0];	
 let filterColumns = [];
 allFilters.forEach((ele) => { filterColumns.push(ele.getAttribute('col-index'))});
    
	var filter_value_dict = {}

// Store value into filter_Value_dict
    allFilters.forEach((filter_i) => {
        col_index = parseInt(filter_i.getAttribute('col-index'));

        value = filter_i.value
        if (value != "all") {
            filter_value_dict[col_index] = value;
        }
    });

    var col_cell_value_dict = {};

    const rows = document.querySelectorAll("#ilptable > tbody > tr")
    rows.forEach((row) => {
        var display_row = true;

        allFilters.forEach((filter_i) => {
            col_index = filter_i.getAttribute('col-index')
            col_cell_value_dict[col_index] = row.querySelector("td:nth-child(" + col_index+ ")").innerHTML
        })

        for (var col_i in filter_value_dict) {
            filter_value = filter_value_dict[col_i]
            row_cell_value = col_cell_value_dict[col_i]
            
            // if (row_cell_value.indexOf(filter_value) == -1 && filter_value != "all") {
            if (filter_value != "all" && row_cell_value != filter_value) {
                display_row = false;
                break;
            }
        }
        if (display_row == true) {
            row.style.display = "table-row"

        } else {
            row.style.display = "none"
        }
    })
};

$('body').on('change', '.table_search-filter', function() {
	filter_rows();
});