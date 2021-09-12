<template>
  <div style="height:1000px" id="maindiv">
    <v-row class="mx-auto" style="margin-top:5%;width:100%">
      <div
        style="margin-left:41%"
        class="btn-group"
        role="group"
        aria-label="Basic example"
      >
        <v-btn
          color="blue"
          @click="showPrevPage()"
          type="button"
          class="btn btn-secondary"
          >Previous Page</v-btn
        >
        <v-btn
          color="blue"
          @click="showNextPage()"
          type="button"
          class="btn btn-secondary"
          >Next Page</v-btn
        >
      </div>
    </v-row>

    <div class="top-bar">
      <span class="page-info">
        Page <span id="page-num"></span> of <span id="page-count"></span>
      </span>
    </div>

    <canvas class="pdfbox" id="pdf-render"></canvas>
  </div>
</template>
<script>
import * as pdfjsLib from "pdfjs-dist";
// const url = "../docs/pdf.pdf";
let pdfDoc = null,
  pageNum = 1,
  pageIsRendering = false,
  pageNumIsPending = null;
const scale = 1.5,
  canvas = document.querySelector("#pdf-render"),
  ctx = 0;
export default {
  props: ["id"],
  created() {
    console.log(ctx);
    this.getDoc();
  },
  methods: {
    async getDoc() {
      let url = "documents/" + this.id;
      console.log(url);
      const pdfjsWorker = await import("pdfjs-dist/build/pdf.worker.entry");
      pdfjsLib.GlobalWorkerOptions.workerSrc = pdfjsWorker;
      pdfjsLib

        .getDocument(url)
        .promise.then((pdfDoc_) => {
          pdfDoc = pdfDoc_;

          document.querySelector("#page-count").textContent = pdfDoc.numPages;

          this.renderPage(pageNum);
        })
        .catch((err) => {
          // Display error
          const div = document.createElement("div");
          div.className = "error";
          div.appendChild(document.createTextNode(err.message));
          document.querySelector("#maindiv").insertBefore(div, canvas);
          // Remove top bar
          document.querySelector(".top-bar").style.display = "none";
        });
    },
    renderPage(num) {
      pageIsRendering = true;

      // Get page
      pdfDoc.getPage(num).then((page) => {
        // Set scale
        const viewport = page.getViewport({ scale });
        //  document.querySelector("#pdf-render"),
        document.querySelector("#pdf-render").height = viewport.height;
        document.querySelector("#pdf-render").width = viewport.width;

        const renderCtx = {
          canvasContext: document.querySelector("#pdf-render").getContext("2d"),
          viewport,
        };

        page.render(renderCtx).promise.then(() => {
          pageIsRendering = false;

          if (pageNumIsPending !== null) {
            this.renderPage(pageNumIsPending);
            pageNumIsPending = null;
          }
        });

        // Output current page
        document.querySelector("#page-num").textContent = num;
      });
    },
    queueRenderPage(num) {
      if (pageIsRendering) {
        pageNumIsPending = num;
      } else {
        this.renderPage(num);
      }
    },
    showNextPage() {
      if (pageNum >= pdfDoc.numPages) {
        return;
      }
      pageNum++;
      this.queueRenderPage(pageNum);
    },

    // Show Prev Page
    showPrevPage() {
      if (pageNum <= 1) {
        return;
      }
      pageNum--;
      this.queueRenderPage(pageNum);
    },
  },
};
</script>
<style scoped>
.pdfbox {
  z-index: 5;
  height: 900px;
  width: 950px;
  overflow-y: scroll;
  border: solid black 2px;
  box-shadow: 1%;
  box-sizing: content-box;
  background-color: gray;
  padding: 2%;
}
</style>
