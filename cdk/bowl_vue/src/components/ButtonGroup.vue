<script setup lang="ts">

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

</script>

<template>
    <ul class='button-group'>
        <slot />
    </ul>
</template>

<style scoped>

.draw-button-group {

    float: left;

    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.6), 0 6px 20px 0 rgba(0,0,0,0.6);
    border-radius: 5px;
    background: radial-gradient(#ff2222, #881133);
}

.draw-button-group li {
    border-left: 2px solid #880000;
}

.draw-button-group li .button {
    color: white;
    font-weight: bold;
    background: none;
}

.draw-button-group li:first-child {
    border-left: none;
}
</style>
