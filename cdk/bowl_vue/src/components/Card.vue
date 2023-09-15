<script setup lang="ts">

import { getCardinality } from '../helpers/getCardinality'
import { getSuit, getSuitName } from '../helpers/getSuit'

defineProps<{
  card: string,
  index: number,
  selected: boolean
}>()




</script>

<template>
    <div :class="['column', 'a-card', getSuitName(card), `card-${index}`, {selected: selected}]" @click="$emit('toggle', {card, index})">
        <div class='cardinality'>
            <span>{{getCardinality(card)}}</span>
        </div>
        <div clas='suit'>
            <span>{{getSuit(card)}}</span>
        </div>
        <div class='big'>
            <div class='suit'>
                <span>{{getSuit(card)}}</span>
            </div>
        </div>
    </div>
                
</template>

<style scoped>

.a-card {
    font-family: 'carddeck';
    font-size: 4em;
    display: block;
    background-color: white;
    height: 450px;
    float: left;
    margin-left: -240px;
    border-radius: 15px;
    box-shadow: -1px 1px 5px #004400;
}
.a-card.selected {
	background-color: black;
	color: white;
	margin-top: -40px;
	border: white solid 1px;
}
    
.a-card.big {
	width: 300px;
}

.a-card.hearts, .a-card.diamonds {
    color: red;
}

.a-card.hearts.selected, .a-card.diamonds.selected {
	color: cyan;
}

.a-card .big .suit span {  
    width: auto;
    font-size: 12rem;
    margin-top: -0.5em;
}           
    
.a-card.card-1 {
    z-index: 305;
}
.a-card.card-2 {
    z-index: 310;
}
.a-card.card-3 {
    z-index: 315;
}
.a-card.card-4 {
    z-index: 320;
}
.a-card.card-5 {
    z-index: 325;
}
.a-card.card-6 {
    z-index: 330;
}
.a-card.card-7 {
    z-index: 335;
}
.a-card.card-8 {
    z-index: 340;
}
.a-card.card-9 {
    z-index: 345;
}
.a-card.card-10 {
    z-index: 350;
}
.a-card.card-11 {
    z-index: 355;
}
.a-card.card-12 {
    z-index: 360;
}
.a-card.card-13 {
    z-index: 365;
}
.a-card.card-14 {
    z-index: 370;
}
.a-card.card-15 {
    z-index: 375;
}   

.a-card .cardinality {
    margin-left: -0.25em;
}

.a-card .cardinality span {
    width: 100px;
    display: block;
    text-align: center;
}
   
.a-card .suit {
    margin-left: -.25em;
    margin-top: -1.5rem;
}

.a-card .suit span {
    width: 100px;
    display: block;
    text-align: center;
}

</style>
