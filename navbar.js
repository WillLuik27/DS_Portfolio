// navbar.js
// Since all files are in the root folder, no need for dynamic baseURL adjustment
const baseURL = '';

document.write(`
<header>
    <h1>Welcome to My Portfolio</h1>
    <nav>
        <ul>
            <li><a href="${baseURL}index.html">Home</a></li>
            <li class="dropdown">
                <a href="#" class="dropbtn">Projects</a>
                <div class="dropdown-content">
                    <a href="${baseURL}scheduler_page.html">Scheduling Optimizer</a>
                    <a href="${baseURL}house_fire_page.html">House Fire Model</a>
                    <a href="${baseURL}forest_fire_page.html">Monte Carlo - Forest Fire</a>
                    <a href="${baseURL}birthrate_page.html">Population Dynamics Model</a>
                    <a href="${baseURL}labor_force_page.html">Male Labor Force Model</a>
                    

                </div>
            </li>
            <li><a href="${baseURL}about.html">About Me</a></li>
            <li><a href="${baseURL}resume.html">Resume</a></li>
        </ul>
    </nav>
</header>
`);
