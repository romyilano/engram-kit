/* Manga flipbook — supports multiple books via ?book= query param ------- */

const BOOKS = {
  "alma": {
    title: "<em>The Notebook That Redesigns Itself</em> — an ALMA explainer",
    pages: [
      {
        src: "manga/alma/panels/alma_page01.png",
        title: "The Forgetful Robot",
        caption: "Foundation models are stateless. Without memory, Engy re-solves the same task from scratch every single time — never carrying anything forward. That statelessness is what bottlenecks an agent's ability to keep learning.",
        purpose: "Page 1 · The problem — no memory means no continual learning."
      },
      {
        src: "manga/alma/panels/alma_page02.png",
        title: "A Box Full of Notes",
        caption: "The common fix: bolt on a memory module so Engy can store and reuse past experience. The chest-notebook fills with notes — but who decides how that notebook is shaped?",
        purpose: "Page 2 · Memory modules let agents retain and reuse experience."
      },
      {
        src: "manga/alma/panels/alma_page03.png",
        title: "Stop Hand-Drawing the Box",
        caption: "Most memory designs are human-crafted and fixed. A box drawn by hand fits one task and breaks on the next — it can't adapt to the diversity and non-stationarity of the real world.",
        purpose: "Page 3 · Hand-crafted, fixed memory designs don't generalize."
      },
      {
        src: "manga/alma/panels/alma_page04.png",
        title: "The Meta Agent's Loop",
        caption: "ALMA meta-learns the memory design itself. A Meta Agent samples a design from the archive, reflects on its code and logs, plans and implements a new design, verifies it, evaluates it on real tasks, then archives the result to guide the next round.",
        purpose: "Page 4 · The open-ended exploration loop at ALMA's core."
      },
      {
        src: "manga/alma/panels/alma_page05.png",
        title: "Memory Is Just Code",
        caption: "The search space is executable code — database schemas plus their retrieval and update mechanisms. Because any memory can be written as code, the space of possible designs is effectively unbounded.",
        purpose: "Page 5 · Code as the search space for arbitrary memory designs."
      },
      {
        src: "manga/alma/panels/alma_page06.png",
        title: "The Design Archive",
        caption: "Every explored design is stored with its evaluation log. The Meta Agent samples from this archive to seed new ideas, so better designs propagate and the search compounds over time.",
        purpose: "Page 6 · The archive of designs + logs drives future search."
      },
      {
        src: "manga/alma/panels/alma_page07.png",
        title: "Four Worlds, One Winner",
        caption: "Tested across ALFWorld, TextWorld, Baba Is AI, and MiniHack, the learned designs consistently beat state-of-the-art human-crafted memory baselines — and are more cost-efficient than most.",
        purpose: "Page 7 · Results across four sequential decision-making domains."
      },
      {
        src: "manga/alma/panels/alma_page08.png",
        title: "Memory That Designs Itself",
        caption: "A step toward self-improving systems that learn to be adaptive, continual learners — when developed and deployed safely. It is exactly the kind of memory ENGRAM asks you to build: one that ingests dated states over time and answers without hindsight.",
        purpose: "Page 8 · The big picture, the open question, and the ENGRAM tie-in."
      }
    ]
  },

  "ama-bench": {
    title: "<em>The Long Road Test</em> — an AMA-Bench explainer",
    pages: [
      {
        src: "manga/ama-bench/panels/amabench_page01.png",
        title: "What Does an Agent Remember?",
        caption: "LLM agents now run long-horizon tasks — navigation, coding, web search. Memory is what keeps them coherent across a long journey. Engy sets out down a very long road.",
        purpose: "Page 1 · Long-horizon agents live or die by their memory."
      },
      {
        src: "manga/ama-bench/panels/amabench_page02.png",
        title: "Not Chit-Chat — Trajectories",
        caption: "Old benchmarks test dialogue. Real agent memory is a trajectory of states, actions, observations, and tool outputs — machine-generated (JSON, ASCII tables, code), causally linked, and objective. No phatic chit-chat.",
        purpose: "Page 2 · Real agent memory is trajectory-shaped, not dialogue-shaped."
      },
      {
        src: "manga/ama-bench/panels/amabench_page03.png",
        title: "Two Halves of the Bench",
        caption: "AMA-Bench pairs a real-world subset — expert QA across Web, open-world QA, Text2SQL, software engineering, gaming, and embodied AI — with a synthetic subset whose rule-based QA scales to any horizon length.",
        purpose: "Page 3 · A real-world subset plus a scalable synthetic subset."
      },
      {
        src: "manga/ama-bench/panels/amabench_page04.png",
        title: "Four Kinds of Question",
        caption: "The Examiner asks four kinds: Temporal Information, State Dependency, Memory Updating, and Memory Summarization — each probing a different way memory can fail.",
        purpose: "Page 4 · The four question categories the benchmark measures."
      },
      {
        src: "manga/ama-bench/panels/amabench_page05.png",
        title: "Why Memory Breaks",
        caption: "Even frontier models struggle — GPT-5.2 reaches only about 72%. Lossy compression and similarity-only retrieval grab superficially-similar notes and miss the causal, objective information the task actually needs.",
        purpose: "Page 5 · Where existing memory systems fall short, and why."
      },
      {
        src: "manga/ama-bench/panels/amabench_page06.png",
        title: "The Causality Graph",
        caption: "AMA-Agent builds a causality graph — actions to state transitions to observations — and uses tool-augmented retrieval. It reaches 57.22%, outperforming the strongest baseline by 11.16%.",
        purpose: "Page 6 · A causality-graph memory with tool-augmented retrieval."
      },
      {
        src: "manga/ama-bench/panels/amabench_page07.png",
        title: "Design Is the Bottleneck",
        caption: "The lesson: it's the memory-system design, not raw model size, that holds agents back. That is the heart of ENGRAM — building memory that ingests dated states over time and answers without hindsight, telling current from stale, superseded, and uncertain.",
        purpose: "Page 7 · The takeaway and the ENGRAM tie-in."
      }
    ]
  }
};

/* ---- select the book ---------------------------------------------------- */
const params = new URLSearchParams(location.search);
const bookId = BOOKS[params.get("book")] ? params.get("book") : "alma";
const BOOK = BOOKS[bookId];
const PAGES = BOOK.pages;

let i = 0;

const img       = document.getElementById("page-img");
const titleEl   = document.getElementById("page-title");
const capEl     = document.getElementById("page-caption");
const purpEl    = document.getElementById("page-purpose");
const numEl     = document.getElementById("page-num");
const prevBtn   = document.getElementById("prev");
const nextBtn   = document.getElementById("next");
const dotsWrap  = document.getElementById("dots");
const thumbs    = document.getElementById("thumbs");
const bookTitle = document.getElementById("book-title");

bookTitle.innerHTML = BOOK.title;
document.title = bookTitle.textContent + " — Manga Flipbook";

function buildNav() {
  PAGES.forEach((p, idx) => {
    const d = document.createElement("button");
    d.setAttribute("aria-label", "Go to page " + (idx + 1));
    d.addEventListener("click", () => go(idx));
    dotsWrap.appendChild(d);

    const t = document.createElement("img");
    t.src = p.src;
    t.alt = "Page " + (idx + 1) + " thumbnail";
    t.loading = "lazy";
    t.addEventListener("click", () => go(idx));
    thumbs.appendChild(t);
  });
}

function render() {
  const p = PAGES[i];
  img.classList.remove("fade");
  void img.offsetWidth; // restart the animation
  img.src = p.src;
  img.alt = "Manga page " + (i + 1) + " — " + p.title;
  img.classList.add("fade");

  titleEl.textContent = p.title;
  capEl.textContent   = p.caption;
  purpEl.textContent  = p.purpose;
  numEl.textContent   = "PAGE " + (i + 1) + " / " + PAGES.length;

  prevBtn.disabled = i === 0;
  nextBtn.disabled = i === PAGES.length - 1;

  [...dotsWrap.children].forEach((d, idx) => d.classList.toggle("active", idx === i));
  [...thumbs.children].forEach((t, idx) => t.classList.toggle("active", idx === i));

  history.replaceState(null, "", "?book=" + bookId + "#p" + (i + 1));
}

function go(idx) {
  i = Math.max(0, Math.min(PAGES.length - 1, idx));
  render();
}
function next() { if (i < PAGES.length - 1) go(i + 1); }
function prev() { if (i > 0) go(i - 1); }

document.getElementById("zone-next").addEventListener("click", next);
document.getElementById("zone-prev").addEventListener("click", prev);
nextBtn.addEventListener("click", next);
prevBtn.addEventListener("click", prev);

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight" || e.key === " ") { e.preventDefault(); next(); }
  if (e.key === "ArrowLeft") { e.preventDefault(); prev(); }
  if (e.key === "Home") go(0);
  if (e.key === "End") go(PAGES.length - 1);
});

// deep-link support: #p3 opens page 3
const m = location.hash.match(/^#p(\d+)$/);
if (m) i = Math.max(0, Math.min(PAGES.length - 1, parseInt(m[1], 10) - 1));

buildNav();
render();
