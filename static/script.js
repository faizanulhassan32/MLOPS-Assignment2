const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})







const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})


// for csv file
function handleFileSelect(event) {
	const file = event.target.files[0];
	if (!file) {
	  return;
	}
	const reader = new FileReader();
	reader.onload = function(event) {
	  const csvData = event.target.result;
	  // Do something with the CSV data, e.g. parse it and display it in a table
	};
	reader.readAsText(file);
  }

  

// for chart
// get a reference to the canvas element
const ordersChart = document.getElementById('orders-chart').getContext('2d');

// create the chart object
const chart = new Chart(ordersChart, {
	type: 'line',
	data: {
		labels: [], // x-axis labels for each data point (empty to start)
		datasets: [{
			label: 'Status',
			data: [], // y-axis data for each data point (empty to start)
			// borderColor: 'rgba(255, 99, 132, 1)',
			fill: false
		}]
	},
	options: {
		responsive: true,
		title: {
			display: true,
			text: 'Recent Orders'
		},
		scales: {
			xAxes: [{
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'Time'
				}
			}],
			yAxes: [{
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'Order Status'
				},
				ticks: {
					min: 0,
					max: 3,
					stepSize: 1,
					callback: function(value, index, values) {
						// map the tick values to the corresponding order status labels
						return ['Completed', 'Pending', 'Process'][value];
					}
				}
			}]
		}
	}
});

// function to add a new data point to the chart
function addDataPoint(label, data) {
	chart.data.labels.push(label);
	chart.data.datasets[0].data.push(data);
	
	// remove the oldest data point if the chart has more than 10 points
	if (chart.data.labels.length > 10) {
		chart.data.labels.shift();
		chart.data.datasets[0].data.shift();
	}
	
	chart.update(); // redraw the chart with the new data
}

// example usage:
setInterval(function() {
	// get the latest data from the server (e.g. using AJAX)
	// let's assume the data is an object with the format {label: status}
	const data = { '2022-03-18T10:30:00': 1, '2022-03-18T10:31:00': 2, '2022-03-18T10:32:00': 0 };
	
	// add each data point to the chart
	for (const [label, value] of Object.entries(data)) {
		addDataPoint(label, value);
	}
}, 60000); // update the chart every minute (adjust as needed)
