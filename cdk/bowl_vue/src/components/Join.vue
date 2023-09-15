<script setup lang="ts">

import { useActions } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])

import Button from './Button.vue'

</script>

<template>
    <div class='join-game'>
        <div class='grid-x row align-center'>
            <div class='column'>
                <input type='text' placeholder='Enter Your Name' />
            </div>
        </div>
        <div class='grid-x row align-center'>
            <div class='column'>
                <input type='text' placeholder='Enter Game ID' />
            </div>
        </div>
        <div class='grid-x row align-center'>
            <div class='column'>
                <Button text='Join Game Now' @click="changeView('Pregame')" />
            </div>
        </div>
    </div>
</template>

<style scoped>

.join-game {

    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    width: 100%;
    
    .draw-button {
        float: none;
        margin-right: 0;
	font-size: 3em;
    }
}

</style>
