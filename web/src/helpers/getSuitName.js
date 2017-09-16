export default function getSuitName(card) {

    let cardPart = card.charAt(1);

    let xlate = {};
    xlate['C'] = 'clubs';
    xlate['D'] = 'diamonds';
    xlate['H'] = 'hearts';
    xlate['S'] = 'spades';

    let xlated = cardPart;
    if(cardPart in xlate) {
        xlated = xlate[cardPart];
    }

    return xlated;
}
