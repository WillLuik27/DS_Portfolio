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
                    <a href="${baseURL}fire_page.html">Fire Model</a>
                    <a href="${baseURL}scheduler_page.html">Scheduling Optimizer</a>
                    <a href="${baseURL}thermal_eq.html">Earth Crust Model</a>

                </div>
            </li>
            <li><a href="${baseURL}about.html">About Me</a></li>
            <li><a href="${baseURL}resume.html">Resume</a></li>
        </ul>
    </nav>
</header>
`);
