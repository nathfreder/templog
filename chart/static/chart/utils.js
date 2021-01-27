/**
 * Get number of days ago in ISO format
 * @param {number} days
 */
function daysAgo(days) {
    const date = new Date();
    date.setDate(date.getDate() - days);
    return date.toISOString();
}

/**
 * Get before and after dates from select value
 * @param {string} select
 */
function getBeforeAfter(select) {
    let before = '';
    let after = '';
    switch (select) {
        case 'day':
            after = daysAgo(1);
            break;
        case 'week':
            after = daysAgo(7);
            break;
        case '2weeks':
            after = daysAgo(14);
            break;
        case 'month':
            after = daysAgo(30);
            break;
    }
    return { before, after }
}