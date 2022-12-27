<script>
    let raw_date = "";
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
