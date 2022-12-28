<script>
    function today() {
        let today = new Date();
        let dd = String(today.getDate()).padStart(2, "0");
        let mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
        let yyyy = today.getFullYear();

        return yyyy + "-" + mm + "-" + dd;
    }

    function to_ddmmyy(raw_date) {
        let split_string = raw_date.split("-");
        split_string = split_string.reverse();
        let ddmmyyyy = split_string.join("");
        let ddmmyy = ddmmyyyy.slice(0, 4) + ddmmyyyy.slice(6);

        return ddmmyy;
    }

    let raw_date = today();
    $: ddmmyy = to_ddmmyy(raw_date);
    let weight = 75;
</script>

<h1>New weight measurement</h1>

<div class="select_container">
    Select your weight: <input
        type="number"
        bind:value={weight}
        min="0"
        max="200"
    /> kg
</div>

<div class="select_container">
    Select the date: <input type="date" bind:value={raw_date} />
</div>
