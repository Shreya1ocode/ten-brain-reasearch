const containerSize = 1024;
const perSlide = 3;
const gapSize = 20;

// numberOfGap = slide - 1 (i.e 2 slides has 1 gap between them)
const numberOfGap = perSlide - 1;
const totalGapSize = gapSize * numberOfGap;

const slideWidth = (containerSize / perSlide) - (totalGapSize / perSlide)

// Explanation:
// 1024px container with 2 slides = 512px per slide
// 2 slides has 20px gap between them
// each slide should reduce their width to form that 20px gap.
// (502px * 2) + 20px = 1024px

// Example 2:
// 1024px container with 3 slides = 341.33px per slide
// 3 slides has total of 40px gaps
// each slide should reduce their width to form that 40px gap.
// (328px * 3) + 40px = 1024px

const grid = document.querySelector('.grid')

grid.style.gridAutoColumns = `${slideWidth}px`;
grid.style.gridGap = `${gapSize}px`;

const prevBtn = document.querySelector('.btn-prev');
const nextBtn = document.querySelector('.btn-next');

let page = 1;

prevBtn.addEventListener('click', () => {
  if (page === 1) {
    return;
  }
  const transformX = (slideWidth + gapSize) * (page - 1);
  grid.style.transform = `translateX(${-transformX}px)`;
  page -= 1;
});

nextBtn.addEventListener('click', () => {
  if (page === grid.childElementCount - perSlide) {
    return;
  }
  const transformX = (slideWidth + gapSize) * (page);
  grid.style.transform = `translateX(${-transformX}px)`;
  page += 1;
});
