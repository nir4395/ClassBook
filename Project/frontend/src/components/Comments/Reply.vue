<template>
     <div class="outerIssuesContainer">
      <!--  inner container for issues -->
            <div class="innerIssuesContainer">
                <div class="issueDiv">
                    <!-- <div>
                        <img class="issueIcon" height="36"  width="36" :src="require(`@/assets/${img}`)" >
                        </div> -->
                    <div class="innerIssueDiv">
                      <div class="innerIssueDivData">
                          <!-- header of reply -->
                        <div class="contentissueDiv"><h4 class="issueDivText">
                                        {{author}}
                            </h4>
                             <div class="issueContent"> 
                                 <!-- content of reply -->
                                 {{content}}
                                  
                                   </div>
                            </div>
                           
                        <div class="ratingDivIssue">
                            <div class="ratings">
                                <div class="ratingValue">{{rating}}
                                     <v-icon color="blue">thumb_up</v-icon>
                                </div>
                                <span class="gapSpan"></span>
                             

                            </div>
                           
                            
                        </div>
                        
                     </div>
                      <div class="issueContent">{{date}} </div>
                    </div>
                </div>
            </div>


      </div >
</template>
<script>
export default {
    props:['author','date','content','rating','img']
}
</script>
<style scoped>
.commentsOnIt{
    color:gray
}
.commentsOnIt:hover{
    color:lightblue
}
.starUnMarked{
    color: gray;
}

.starUnMarked:hover{
    color: gold;
}
.gapSapn{
    position: absolute;
    width: 1px;
    height: 1px;
    margin: -1px;
    padding: 0;
    overflow: hidden;
    clip: rect(0,0,0,0);
    border: 0;
}
.iconrating{
    font-family: udemyicons!important;
    speak: none;
    font-style: normal;
    font-weight: 400;
    font-variant: normal;
    text-transform: none;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    vertical-align: 0;
}
.ratings{
    display: flex;
    align-items: center;
    justify-content: flex-end;
}
.ratebutton{
    display: inline-block;
    margin-bottom: 0;
    font-weight: 700;
    text-align: center;
    vertical-align: middle;
    touch-action: manipulation;
    cursor: pointer;
    background-image: none;
    border: 1px solid transparent;
    white-space: nowrap;
    padding: 11px 12px;
    font-size: 15px;
    line-height: 1.35135;
    border-radius: 0;
    color: #3e4143;
    background-color: transparent;
    border: 1px solid transparent;
    padding: 10px 11px;
    color: #d1d7dc;
    border-radius: 50%;
    margin-left: -4px;
}
.issueContent{
    margin-top: .4rem;
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.ratingValue{
    font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    display: inline-block;
    color: #3e4143;
    font-weight: 700;
    position: relative;
    vertical-align: bottom;
    z-index: 1;
}
.hrefIssue{
    color: #1c1d1f;
    font-weight: 700;
}
.issueDivText{
      font-family: sf pro display,-apple-system,BlinkMacSystemFont,Roboto,segoe ui,Helvetica,Arial,sans-serif,apple color emoji,segoe ui emoji,segoe ui symbol;
    font-size: 14px;
    font-weight: 700;
    line-height: 1.43em;
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width:60rem;

}
.ratingDivIssue{
    display: flex;
    flex-direction: column;
}
.innerIssueDiv{
  flex: 1;
    min-width: 1px;
    padding-left: 1.6rem;



}
.contentissueDiv{
    display: block;
    flex: 1;
    min-width: 1px;
    padding-right: 4.8rem;



}
.innerIssueDivData{
    display: flex;
    border-top: 1px solid #f7f9fa;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    padding: 1.6rem 2.4rem;


}
 .issueIcon{
   display: inline-block;
    position: relative;
    max-width: 100%;
        border-radius: 50%;
    object-fit: cover;
 }
.innerIssuesContainer{
  border-top: 0;
      border-bottom: 1px solid #f7f9fa;
      display: block

}
.outerIssuesContainer{
      margin-bottom: 48px;
          display: block;

    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
.issueDiv{
  display: flex;
    border-top: 1px solid #f7f9fa;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    padding: 1.6rem 2.4rem;


}



</style>