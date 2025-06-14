<template>
    <div>
        <label>Series Date</label><input v-model='seriesBinding' />
        <br /><br />
        <button @click='getToday'>Today</button> | <button @click='letsGo'>Lets Go!</button>
    </div>
</template>

<style>

</style>

<script setup>
    import { storeToRefs } from 'pinia';
    import { computed, ref } from 'vue';
    import { useStartHereStore } from '../stores/start';
    import { useRouter } from 'vue-router';

    const startHereStore = useStartHereStore();
    const startHere = storeToRefs(startHereStore);
    const router = useRouter();

    const getToday = () => {
        const t = new Date().toISOString();
        console.log(t.slice(0,10));
        startHereStore.setDate(t.slice(0,10));
    };

    const letsGo = () => {
        router.push(`/series/${seriesBinding.value}`);
    };

    const seriesBinding = computed({
        get() {
            return startHere.getSeriesDate.value;
        },
        set(value) {
            console.log(`setting...${value}`);
            startHereStore.setDate(value);
        }
    });

</script>
