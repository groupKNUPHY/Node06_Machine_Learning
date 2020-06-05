void gen(){


	TFile *f1 = new TFile("test.root","recreate");
	TTree *mytree = new TTree("tree","tree");
	
  	double Feature1;
  	double Feature2;
	bool   isSig;

	mytree-> Branch("Feature1",&Feature1);
	mytree-> Branch("Feature2",&Feature2);
	mytree-> Branch("isSig",&isSig);

	for(int i=0; i<5000; i++){
		Feature1 = gRandom->Gaus(3,4);
		Feature2 = gRandom->Gaus(3,3);
		isSig = true;
		mytree->Fill();
	}

	f1->Write();




}
