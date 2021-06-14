var rows = []

main()

function main() {
  for (var i = 0; i < 10; i++) {
    addRow()
  }
  console.log(rows)
  let container = document.querySelector('#rows')
  for (var i = 0; i < rows.length; i++) {
    let newRow = document.createElement('div')
    newRow.innerHTML = rows[i].join(' ')
    container.appendChild(newRow)
  }
}

function addRow() {
  if (rows.length) {
    let lastRow = rows[rows.length-1]
    let newRow = []
    for (var i = 0; i < lastRow.length; i++) {
      newRow.push(lastRow[i])
      if (lastRow[i+1]) {
        newRow.push(lastRow[i]+lastRow[i+1])
      }
    }
    rows.push(newRow)
  } else {
    rows.push([ '<', '>' ])
  }
}
