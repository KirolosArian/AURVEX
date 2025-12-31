const fs = require('fs');
const path = 'code.html';
const s = fs.readFileSync(path, 'utf8');
const start = s.indexOf('const translations =');
const end = s.indexOf('};', start);
if (start === -1 || end === -1) { console.error('Could not find translations block'); process.exit(1); }
const block = s.substring(start, end+2);
console.log('Block length', block.length);
try {
  // try to extract RHS only
  const rhsStart = block.indexOf('=')+1;
  const rhs = block.substring(rhsStart).trim();
  // wrap in parentheses to eval as expression
  new Function('return ' + rhs);
  console.log('Parse succeeded');
} catch (err) {
  console.error('Parse error:', err.message);
  console.error(err.stack);
}
