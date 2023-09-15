<script setup lang="ts">

defineProps<{
  name: string
}>()

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

const cards = ['AS', 'TD', '3S'];


</script>

<template>
    <div class='poker-table-player column'>
        <div class='player-name'>{{name}}</div>
        <div class='player-cards'>
           <span v-for="(card, i) in cards" class='player-card' key="`card-${i}`"></span>
           <span v-show="cards.length > 5" class='extra-cards'>{{`${cards.length - 5}`}}</span>
        </div>
    </div>
</template>

<style scoped>

.poker-table-player {

    padding: 10px;
    margin: 10px;
    border: 2px solid black;
    background: radial-gradient(#888888, #444444);
    color: white;
    border-radius: 5px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.6), 0 6px 20px 0 rgba(0,0,0,0.6);
    
    
    @font-face {
        font-family: 'carddeck';
        src: url('/static/CARDC___.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }
    
    font-family: 'carddeck';
    font-size: 1.25em;
    
    .player-name {
        &.is-finished {
            color: #00ff00;
        }
    }
    
    .player-cards {
        margin-top: 5px;
	
        span {
            display: inline-block;
            color: none;
            height: 1.5em;
            
        }
        .player-card {
            width: 1em;
            background-color: white;
            border-radius: 2px;
            margin-left: -0.5em;
            border: 1px solid #444444;
        }
	
        .player-card:first-child {
            margin-left: auto;
        }
	
        .extra-cards {
            margin-left: 0.5em;
            vertical-align: 5px;
        }	
    }   
}

</style>
