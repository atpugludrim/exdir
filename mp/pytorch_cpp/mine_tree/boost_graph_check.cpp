#include<iostream>
#include<vector>
#include<boost/graph/adjacency_list.hpp>
#include<boost/property_map/property_map.hpp>
using namespace boost;
using namespace std;
int main(int argc, char* argv[]){
    struct myname_t { typedef vertex_property_tag kind;};
    typedef property<myname_t, int> myname;
    struct myedgename_t { typedef edge_property_tag kind;};
    typedef property<myedgename_t, int> myedgename;
    typedef adjacency_list<vecS, vecS, directedS, myname, myedgename> Graph;
    int N, M, u, v;
    cin >> N;
    Graph g(N);
    vector<int> vertices;
    for(int i=0;i<N;i++){
        cin >> v;
        vertices.push_back(v);
    }
    cin >> M;
    for(int i=0;i<M;i++){
        cin >> u >> v;
        add_edge(u, v, g);
    }
    property_map<Graph, myname_t>::type name_map = get(myname_t(), g);
    int c=0;
    for(vector<int>::iterator it=vertices.begin();it!=vertices.end();it++){
        name_map[c++] = *it;
    }
    property_map<Graph, myedgename_t>::type edgename_map = get(myedgename_t(), g);
    int i;
    graph_traits<Graph>::edge_iterator ei, ei_end;
    for(boost::tie(ei, ei_end)=edges(g); ei!=ei_end;++ei){
        cin >> i;
        edgename_map[*ei]=i;
    }
    cin >> i;
    auto neighbors = adjacent_vertices(i, g);
    for (auto vd : make_iterator_range(neighbors))
        cout << vertices[i] << " has adjacent vertex "<< vertices[vd] << "\n";
    graph_traits<Graph>::out_edge_iterator out_i, out_end;
    for(boost::tie(out_i, out_end)=out_edges(i,g); out_i!=out_end;++out_i){
        auto curEdge = *out_i;
        auto curNeighbor = boost::target(curEdge, g);
        cout << curNeighbor << " " << curEdge << " " << edgename_map[curEdge] << "\n";
    }
    return 0;
}
