<script setup lang="ts">

import { store } from './store'

</script>

<template>
    <div class='create-game'>
        <div class='grid-x row align-center'>
            <div class='column'>
                <input type='text' placeholder='Enter Your Name' />
            </div>
        </div>
        <div class='grid-x row align-center'>
            <div class='column'>
                <Button text='Play Now!' />
            </div>
        </div>
    </div>
</template>

<style scoped>

.create-game {
    
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
	margin-top: 0.5em;
	margin-bottom: 0.5em;
    }
}

</style>
