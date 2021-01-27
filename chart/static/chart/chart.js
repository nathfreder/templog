google.charts.load('current', {packages: ['corechart', 'line']})
    .then(drawDashboard);

/**
 * Fetch temperatures from API
 * @return {Promise<any>}
 * @param {string} before
 * @param {string} after
 */
async function fetchData(
    // default is current select value
    before = getBeforeAfter(document.getElementById('date-range').value).before,
    after = getBeforeAfter(document.getElementById('date-range').value).after
) {
    const response = await fetch('/api/temps/?' + new URLSearchParams({
        date_before: before,
        date_after: after,
    }));
    return await response.json()
}

/**
 * Generate data table from data
 * @return {Promise<google.visualization.DataTable>}
 */
async function generateDataTable(before, after) {
    const dataTable = new google.visualization.DataTable();

    // add columns
    dataTable.addColumn('date', 'Date');
    dataTable.addColumn('number', 'Temperature');

    // fetch temp data from api
    const data = await fetchData(before, after);

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
async function drawDashboard(before, after) {
    // get data table
    const data = await generateDataTable(before, after);

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

    // get date range
    const select = document.getElementById('date-range');

    // redraw chart when date range changes
    select.onchange = function () {
        const { before, after } = getBeforeAfter(select.value);
        drawDashboard(before, after);
    }
}
