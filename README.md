<div class="panel panel-default" data-ng-show="document || header">
	<div class="panel-heading">
		<h4 class="panel-title" data-ng-if="document">
			<!-- Once document name is stored in mongoDB, the document type
                property may need to change to match the property on the document
                object rather than the 'hack' used in the case-db.js file -->
			{{document.documentType }} ({{ document.name }})
		</h4>
		<h4 class="panel-title" data-ng-if="header">
			<!-- Once document name is stored in mongoDB, the document type
                property may need to change to match the property on the document
                object rather than the 'hack' used in the case-db.js file -->
			{{ header.displayName }} {{ header.dateReceived | date: "MM/dd/yyyy" }}
		</h4>
	</div>



	<div class="panel-body">

		<div ng-if="loadingDocument">
			<img src="images/ajax-loader.gif" /> Loading Document...
		</div>

		<div ng-show="!loadingDocument">

			<div data-ng-show="pagingInfo">

				<span data-ng-show="!pagingInfo.pages || pagingInfo.pages.length === 0">
                    No text available for this document.
                </span>

				<!--<span data-ng-show="pagingInfo.pages && pagingInfo.pages.length">

                    Page {{currentPage}} of {{ pagingInfo.pages.length }}, Words {{ (pagingInfo.pages[currentPage-1].startPos / 6) | number : 0 }} -
                    {{ (pagingInfo.pages[currentPage-1].endPos / 6) | number : 0 }} of {{ pagingInfo.totalWordCount | number }}

                </span>-->

				<!-- Angular Paging Directive (see bw.paging)
                    page = page currently being displayed
                    page-size = how many items in the list to display on a page
                    total = total count of pages in the list (pages in the document)
                -->
				<div class="document-paging">
					<div paging page="currentPage" page-size="1" total="pagingInfo.pages.length" paging-action="setPage(page)">
					</div>
				</div>


				<div>
					<!--Display the actual document text
                        as html-->
					<!--<div ng-show="thePage && thePage.text" compile="thePage"></div>-->
					<div infinite-scroll='loadMorePages()' infinite-scroll-distance='2' infinite-scroll-up='loadEarlierPages();' infinite-scroll-disabled='pagingInfo.pages.length < 11'>
						<div ng-repeat="page in pagesShown track by $index">
							<a id="anchor{{page.pageNumber}}" class="page-anchor"></a>
							<div compile="page"></div>

							<hr/>
							<span>End of page {{page.pageNumber}}</span>
							<hr/>
						</div>
					</div>
					<!--<div ng-show="!thePage || !thePage.text">
						<b>No text available</b>
					</div>-->
					<!--Display the document text (raw)
                    {{pagingInfo.pages[currentPage-1].text}}-->
				</div>

				<!-- Display the paging info again below the document page -->
				<!--<div paging page="currentPage" page-size="1" total="pagingInfo.pages.length" paging-action="gotoAnchor(page)" style="position:fixed;">
				</div>

				<span data-ng-show="pagingInfo.pages && pagingInfo.pages.length">

                    Page {{currentPage}} of {{ pagingInfo.pages.length }}, Word Count {{ (pagingInfo.pages[currentPage-1].startPos / 6) | number : 0 }} -
                    {{ (pagingInfo.pages[currentPage-1].endPos / 6) | number : 0 }} of {{ pagingInfo.totalWordCount | number : 0}}

                </span>-->

			</div>

		</div>

	</div>

</div>

<div ng-show="showTheDiv" class="annotation-options" id="document-popover" ng-mouseleave="removePopover()">
    <div class="popover-arrow">
        <ul>
        <li><button class="annotation-hover" ng-click="toggleInfo()"> {{pageData.resourceTable.DETAILS}}</button></li>
        <li><button class="annotation-hover" ng-click="searchForAnnotation()">{{pageData.resourceTable.SEARCH_THE_ANNOTATION}}</button></li>
        <li><button class="annotation-hover" ng-click="openDocumentInDMA()">{{pageData.resourceTable.OPEN_DOCUMENT_IN_DMA}}</button></li>
        </ul>
    </div>
</div>

<div id="annInfo" ng-show="showInfo">
	<annotation-information-popup-directive show-info="showInfo" displayed-snippet="displayedSnippet"></annotation-information-popup-directive>
</div>
