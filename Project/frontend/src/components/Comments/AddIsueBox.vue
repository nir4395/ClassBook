<template>
  <div style="height:250px">
    <div class="form-group">
      <div class="labelNewIssue"><b>Details</b></div>
      <div>
        <div class="issuecontainerMenu">
          <div class="issueMenu">
            <div class="btn-group">
              <button
                aria-label="Bold"
                @click="MakeFontBold()"
                class="btn-btn-link menubtnIssue"
              >
                <span class="fas fa-bold"></span>
              </button>
              <button
                aria-label="Italic"
                @click="MakeFontItalic()"
                class="btn-btn-link menubtnIssue"
              >
                <span class="fas fa-italic"></span>
              </button>
              <button
                aria-label="Link"
                @click="addLink()"
                class="btn-btn-link menubtnIssue"
              >
                <span class="fas fa-link"></span>
              </button>
              <button aria-label="Image" class="btn-btn-link menubtnIssue">
                <span class="far fa-image"></span>
              </button>
              <button aria-label="Code" class="btn-btn-link menubtnIssue">
                <span class="fas fa-file-code"></span>
              </button>
            </div>
            <div style="flex: 1;min-width: 1px;"></div>
          </div>
          <div class="issueContainerDetails">
            <div
              id="detailsContent"
              contentEditable="true"
              class="issueDetails"
            >
              <p style="text-align:left" id="contentofIssue">
                Enter Comment Here
              </p>
            </div>
          </div>
        </div>

        <LinkModal
          ref="linkModal"
          v-show="isModalVisible"
          @close="closeModal"
        />
      </div>
    </div>
  </div>
</template>
<script>
import LinkModal from "../Comments/LinkModal.vue";
export default {
  components: {
    LinkModal,
  },

  data() {
    return {
      isModalVisible: false,
      isFontBold: false,
      isFontItalic: false,
    };
  },
  methods: {
    submitnewIssue() {
      var textofIssue = document.getElementById("detailsContent");

      return { content: textofIssue.innerText };
    },
    addLink() {
      this.isModalVisible = true;
    },
    closeModal(value) {
      this.isModalVisible = false;
      if (value !== {}) {
        var hrefDiv = document.createElement("div");
        var link = document.createElement("a");
        link.setAttribute("href", value.url);
        link.setAttribute("rel", "noopener noreferrer");
        link.innerText = value.text;
        hrefDiv.append(link);
        document.getElementById("contentofIssue").appendChild(hrefDiv);
      }
    },
    MakeFontBold() {
      if (this.isFontBold == false) {
        document.getElementById("detailsContent").style.fontWeight = "700";
        this.isFontBold = true;
      } else {
        document.getElementById("detailsContent").style.fontWeight = "";
        this.isFontBold = false;
      }
    },

    MakeFontItalic() {
      if (this.isFontItalic == false) {
        document.getElementById("detailsContent").style.fontStyle = "italic";
        this.isFontItalic = true;
      } else {
        document.getElementById("detailsContent").style.fontStyle = "";
        this.isFontItalic = false;
      }
    },
  },
};
</script>
<style scoped>
.labelNewIssue {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.43em;
  margin: 16px 0 8px;
}
.addNewIssueTitleInput {
  border: 1px solid black;
  height: 34px;
  padding: 0 10px;
  font-size: 13px;
  line-height: 1.287;
  border-radius: 0;
}
.issuecontainerMenu {
  background: #fff;
  z-index: 1000;
}
.menubtnIssue {
  border: none;
  background-color: white;
}
.issueMenu {
  border: 1px solid #1c1d1f;
  border-bottom: 0;
  display: flex;
}
.issueContainerDetails {
  background: #fff;
  font-size: 15px;
  line-height: 1.43;
}
.issueDetails {
  height: 200px;
  background: 0 0;
  border: 1px solid #1c1d1f;
  overflow: auto;
  padding: 20px;
  position: relative;
}
</style>
