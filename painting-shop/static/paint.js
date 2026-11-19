(() => {
  const cv = document.getElementById('sky'), cx = cv.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Pigments from the top of the sky down to the ground
  const stops = [[0, [20, 40, 90]], [.4, [59, 75, 168]], [.68, [48, 130, 150]], [.8, [232, 185, 35]],
                 [.82, [47, 127, 111]], [1, [20, 70, 70]]];
  let W, H, raf, timer, lastW = 0;

  const seeded = a => () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };

  const color = (y, rnd) => {
    const t = Math.min(1, y / H); let k = 1;
    while (k < stops.length - 1 && stops[k][0] < t) k++;
    const [t0, c0] = stops[k - 1], [t1, c1] = stops[k], f = Math.min(1, Math.max(0, (t - t0) / (t1 - t0)));
    return `rgb(${c0.map((v, j) => Math.round(v + (c1[j] - v) * f + (rnd() - .5) * 36)).join(',')})`;
  };

  // Brush direction: slow waves plus a few swirls in the sky
  const angle = (x, y, ground, swirls) => {
    if (ground) return Math.sin(x * .01 + y * .02) * .5;
    const a = Math.sin(x * .005 + Math.sin(y * .007)) * 1.4;
    let vx = Math.cos(a), vy = Math.sin(a);
    for (const [ox, oy] of swirls) {
      const dx = x - ox, dy = y - oy, d = Math.hypot(dx, dy) + 1, w = 2 * Math.exp(-d / (W * .18));
      vx += -dy / d * w; vy += dx / d * w;
    }
    return Math.atan2(vy, vx);
  };

  function paint(animate) {
    cancelAnimationFrame(raf);
    const dpr = Math.min(devicePixelRatio || 1, 1.5);
    W = innerWidth; H = innerHeight; lastW = W;
    cv.width = W * dpr; cv.height = H * dpr; cx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cx.lineCap = cx.lineJoin = 'round';
    const rnd = seeded(7), total = Math.min(7000, W * H / 160 | 0), horizon = H * .8;
    const swirls = [[.72, .2], [.25, .12], [.5, .48]].map(([a, b]) => [a * W, b * H]);
    let i = 0;
    const stroke = () => {
      let x = rnd() * W, y = rnd() * H * 1.02;
      const ground = y > horizon, n = 8 + rnd() * 14 | 0;
      cx.lineWidth = ground ? 6 + rnd() * 8 : 8 + rnd() * 14;
      cx.strokeStyle = color(y, rnd);
      cx.beginPath(); cx.moveTo(x, y);
      for (let k = 0; k < n; k++) { const a = angle(x, y, ground, swirls); x += Math.cos(a) * 4; y += Math.sin(a) * 4; cx.lineTo(x, y); }
      cx.stroke();
    };
    const batch = () => {
      const end = animate ? Math.min(total, i + total / 80) : total;
      while (i < end) { stroke(); i++; }
      if (i < total) raf = requestAnimationFrame(batch);
    };
    batch();
  }

  paint(!reduce);
  addEventListener('resize', () => { clearTimeout(timer); timer = setTimeout(() => { if (innerWidth !== lastW) paint(false); }, 200); });
})();
