<script setup lang="ts">
defineProps<{
  text: string
}>()
</script>

<template>
    <div class='draw-button' @click="$emit('click')">
        <a href='#' class='button'>
            <div class='inner-box'>{{text}}</div>
        </a>
    </div>
</template>

<style scoped>

.draw-button {
    float: left;
    margin-right: 2em;
    font-size: 1.5em;

    .button {
        background: radial-gradient(yellow, orange);
        padding-left: 40px;
        padding-right: 40px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.6), 0 6px 20px 0 rbga(0,0,0,0.6);
        border-radius: 5px;
    }
}

.draw-button.disabled .button {
    background: radial-gradient(#e0e0e0, #c0c0c0);
    color: #a0a0a0;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.25), 0 6px 20px 0 rgba(0,0,0,0.25);
}

.draw-button-group {

    float: left;
    margin-left: auto;

    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.6), 0 6px 20px 0 rgba(0,0,0,0.6);
    border-radius: 5px;
    background: radial-gradient(#ff2222, #881133);
}

.draw-button-group li {
    border-left: 2px solid #880000;
}

.draw-button-group li .button {
    color: white;
    background: none;
    font-size: 1.5em;
}

.draw-button-group li:first-child {
    border-left: none;
}

</style>
