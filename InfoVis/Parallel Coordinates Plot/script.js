let jsonData = [];
const sampling_step = 10;

// Languages available in the dataset
const languages = ['DE', 'ENGB', 'ES', 'FR', 'PTBR', 'RU'];

// Load all data for each language and store it in jsonData
Promise.all(languages.map(lang => plot_language_data(lang)))
    .then(() => {
        calculateGlobalRanges(); // Calculate ranges after all data is loaded
        updatePlot(globalRanges["views"], 'parallel-coordinates-plot') // adjsut according to whatever range is required
        updatePlot([50000, 1000000], 'parallel-coordinates-plot-1'); // First PCP with views range [50000, 1000000]
        updatePlot([0, 50000], 'parallel-coordinates-plot-2');        // Second PCP with views range [0, 50000]
    })
    .catch(error => console.error('Error loading data:', error));


// Store attribute ranges to maintain consistency
const globalRanges = {};

// Function to load data for a language
async function plot_language_data(lang) {
    try {
        const response = await fetch(`../twitch/${lang}/musae_${lang}_target.csv`);
        const data = await response.text();

        const rows = data.trim().split('\n');
        const headers = rows[0].split(',');

        // Parse CSV and add language field
        const langData = rows.slice(1).map(row => {
            const values = row.split(',');
            const rowData = headers.reduce((obj, header, index) => {
                obj[header] = values[index];
                return obj;
            }, {});
            rowData.language = lang; // Add language field
            return rowData;
        });

        // Append to the main jsonData array
        jsonData = jsonData.concat(langData);
        console.log(`Data loaded for ${lang}:`, langData);
    } catch (error) {
        console.error(`Error fetching the file for ${lang}:`, error);
    }
}

// Function to calculate consistent global ranges for each attribute
function calculateGlobalRanges() {
    const attributes = ['days', 'views'];
    attributes.forEach(attr => {
        const values = jsonData.map(row => +row[attr]);
        globalRanges[attr] = [Math.min(...values), Math.max(...values)];
    });
}

// Update plot function
function updatePlot(viewsRange, elementId) {
    if (jsonData.length === 0) {
        console.error('Data not loaded yet.');
        return;
    }

    const selectedDimensions = [];
    const sampledData = jsonData.filter((_, index) => index % sampling_step === 0);

    // Configure dimensions, using the custom viewsRange for 'Views'
    if (document.getElementById('days').checked) {
        selectedDimensions.push({
            label: 'Days',
            values: sampledData.map(row => +row.days),
            range: globalRanges.days,
            constraintrange: globalRanges.days
        });
    }
    if (document.getElementById('views').checked) {
        selectedDimensions.push({
            label: 'Views',
            values: sampledData.map(row => +row.views),
            range: viewsRange,             // Use custom views range
            constraintrange: viewsRange
        });
    }
    if (document.getElementById('partner').checked) {
        selectedDimensions.push({
            label: 'Partner',
            values: sampledData.map(row => row.partner === 'True' ? 1 : 0),
            tickvals: [0, 1],
            ticktext: ['No', 'Yes'],
            constraintrange: [0, 1]
        });
    }
    if (document.getElementById('lang').checked) {
        selectedDimensions.push({
            label: 'Language',
            values: sampledData.map(row => languages.indexOf(row.language)),
            tickvals: languages.map((_, i) => i),
            ticktext: languages,
            constraintrange: [0, languages.length - 1]
        });
    }

    // Convert mature column to numeric for color mapping
    const mature = sampledData.map(row => row.mature === 'True' ? 1 : 0);

    // Create the plot with reordering enabled
    const trace = {
        type: 'parcoords',
        line: {
            color: mature,
            colorscale: [[0, 'blue'], [1, 'red']],
            showscale: true,
            colorbar: {
                title: "Mature Content"
            }
        },
        dimensions: selectedDimensions
    };

    const layout = {
        title: `Interactive Twitch User Data - Views Range [${viewsRange[0]}, ${viewsRange[1]}]`,
        plot_bgcolor: 'white',
        paper_bgcolor: 'white'
    };

    Plotly.newPlot(elementId, [trace], layout);
}