<template>
    <div class="header">
        <span>
            <button :disabled='!display.getGameLeft'>&lt;&lt;</button>
        </span> | 
        <span>
            <button :disabled='!display.getFrameLeft'>Previous Frame</button>
        </span> | 
        <span>
            <button :disabled='!display.getFrameRight'>Next Frame</button>
        </span> | 
        <span>
            <button :disabled='!display.getGameRight'>&gt;&gt;</button>
        </span>
    </div>

    <div>
        <table>
            <tr>
                <td colspan='display.getFrameNumber.value === 10 ? 3 : 2'>
                    {{ display.getFrameNumber }}
                </td>
            </tr>
            <tr>
                <td v-for="t in display.getFrameThrows.value">
                    {{ t }}
                </td>
            </tr>
            <tr>
                <td colspan='display.getFrameNumber.value === 10 ? 3 : 2'>
                    {{ display.getFrameScore }}
                </td>
            </tr>
        </table>
    </div>

</template>

<script setup>
    import { storeToRefs } from 'pinia';
    import { useDisplayStore } from '../stores/display';

    const display = storeToRefs(useDisplayStore());

    //const frames = display.getMaster.value.gameData[display.getGameNumber.value].frames;
    //const fs = frames.map((e) => e.frameNumber);
    //console.log(fs);
    //.map((e) => e.frameNumber)
    //console.log(`${display.getFrameNumber} :: ${frames}`);
    //console.log(display.getMaster.value.gameData[display.getFrameNumber.value].frames);
    console.log(display.getGameLeft.value)
    console.log(display.getFrameLeft.value)
    //console.log(display.getFrameRight.value)

</script>
