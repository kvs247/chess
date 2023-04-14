import moment from 'moment';

export function pgnToObj(pgn) {
    const pgnObj = {
        
    };

    if (!pgn) return pgnObj;

    const dateRegex = /Date "(.*)"/;
    const dateRaw = dateRegex.exec(pgn)[1];
    const yyyymmdd = dateRaw.split('.');
    const date = new Date(yyyymmdd[0], yyyymmdd[1]-1, yyyymmdd[2]);
    const formattedDate = moment(date).format('MMMM D Y');
    pgnObj['date'] = formattedDate;

    const resultRegex = /Result "(.*)"/;
    const result = resultRegex.exec(pgn)[1];
    pgnObj['result'] = result;

    const whiteUsernameRegex = /White "(.*)"/;
    const whiteUsername = whiteUsernameRegex.exec(pgn)[1];
    pgnObj['whiteUsername'] = whiteUsername;

    const blackUsernameRegex = /Black "(.*)"/;
    const blackUsername = blackUsernameRegex.exec(pgn)[1];
    pgnObj['blackUsername'] = blackUsername;

    // not all pgns have this :(
    // const playCountRegex = /PlayCount "(.*)"/;
    // const playCount = playCountRegex.exec(pgn)[1];
    // pgnObj['playCount'] = playCount;

    const pgnSplit = pgn.split('\n');
    const moveListSplit = pgnSplit.slice(pgnSplit.indexOf('') + 1);
    const moveList = moveListSplit.join(' ');
    pgnObj['moveList'] = moveList;

    return pgnObj;
}

export function fenToArray(fen) {
    const piecesString = fen.split(' ')[0].replace(/\//g, '');
    const piecesArrayNums = piecesString.split('');
    const piecesArray = piecesArrayNums.map(piece => {
      if (parseInt(piece)) {
        return [...Array(parseInt(piece)).fill(null)];
      };
      return piece;
    }).flat();
    return piecesArray;
  }