window.addEventListener(
 'load',
 (event) => {
        let today = new Date();
        let year = today.getFullYear();
        let month = today.getMonth() + 1; 
        let day = today.getDate();

        let formattedDate = `${year}, ${month}, ${day}`;

        document.getElementById('date').textContent = formattedDate;
}
);