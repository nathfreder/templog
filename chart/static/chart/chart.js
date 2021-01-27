google.charts.load('current', {packages: ['corechart', 'line']})
    .then(drawDashboard);

/**
 * Fetch temperatures from API
 * @return {Promise<any>}
 */
async function fetchData() {
    const response = await fetch('/api/temps');
    return await response.json()
}

/**
 * Generate data table from data
 * @return {Promise<google.visualization.DataTable>}
 */
async function generateDataTable() {
    const dataTable = new google.visualization.DataTable();

    // add columns
    dataTable.addColumn('date', 'Date');
    dataTable.addColumn('number', 'Temperature');

    // fetch temp data from api
    const data = await fetchData();

    // map over rows and reformat for data table
    const rows = data.map(function (temp) {
        // [parsed date, temp celsius float]
        return [new Date(temp.date), temp.temperature];
    });

    // add rows to data table
    dataTable.addRows(rows);

    // add celsius to tooltip
    const tempFormatter = new google.visualization.NumberFormat({
        suffix: 'ºC',
        fractionDigits: 0
    });

    // add time & date to tooltip
    const dateFormatter = new google.visualization.DateFormat({
        pattern: "MMM d, yyyy, h:mm aa"
    });

    tempFormatter.format(dataTable, 1);
    dateFormatter.format(dataTable, 0);

    return dataTable;
}

/**
 * Draw dashboard
 * @return {Promise<void>}
 */
async function drawDashboard() {
    // get data table
    const data = await generateDataTable();

    // create line chart
    const chart = new google.visualization.LineChart(document.getElementById('chart'));

    // render chart and filter
    chart.draw(data, {
            hAxis: {
                title: 'Date'
            },
            vAxis: {
                title: 'Temperature',
                format: '#ºC'
            },
            legend: {
                position: 'none'
            }
    });
}
